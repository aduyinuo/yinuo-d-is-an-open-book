// Publish the Annotated Slides integration to GitBook.
//
// Needs one thing from you: a GitBook personal access token, from
// https://app.gitbook.com/account/developer
//
// Everything else — finding your organization, patching the manifest,
// authenticating the CLI, publishing — happens here.
//
//   node publish.mjs                 (prompts for the token)
//   node publish.mjs <token>         (or pass it)
//   GITBOOK_TOKEN=... node publish.mjs

import { readFileSync, writeFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createInterface } from 'node:readline/promises';
import { stdin, stdout } from 'node:process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const MANIFEST = join(HERE, 'gitbook-manifest.yaml');
const API = 'https://api.gitbook.com/v1';

function die(msg) {
    console.error(`\n  ${msg}\n`);
    process.exit(1);
}

async function ask(question) {
    const rl = createInterface({ input: stdin, output: stdout });
    const answer = (await rl.question(question)).trim();
    rl.close();
    return answer;
}

async function api(path, token) {
    const res = await fetch(`${API}${path}`, {
        headers: { Authorization: `Bearer ${token}` },
    });
    if (res.status === 401) die('That token was rejected. Make a new one at https://app.gitbook.com/account/developer');
    if (!res.ok) die(`GitBook API returned ${res.status} for ${path}\n  ${await res.text()}`);
    return res.json();
}

// ---------------------------------------------------------------- token

let token = process.argv[2] || process.env.GITBOOK_TOKEN;
if (!token) {
    console.log('\n  Open https://app.gitbook.com/account/developer and create a personal access token.');
    console.log('  It is not written into this repository.\n');
    token = await ask('  Paste the token here: ');
}
if (!token) die('No token given.');

// ---------------------------------------------------------------- who

const me = await api('/user', token).catch(() => null);
if (me?.displayName) console.log(`\n  Signed in as ${me.displayName}.`);

// ---------------------------------------------------------------- org

const { items: orgs = [] } = await api('/orgs', token);
if (orgs.length === 0) die('That account has no GitBook organization.');

let org;
if (orgs.length === 1) {
    org = orgs[0];
    console.log(`  Organization: ${org.title} (${org.id})`);
} else {
    console.log('\n  Which organization?\n');
    orgs.forEach((o, i) => console.log(`    ${i + 1}. ${o.title}  (${o.id})`));
    const pick = Number(await ask('\n  Number: '));
    org = orgs[pick - 1];
    if (!org) die('Not one of the choices.');
}

// ---------------------------------------------------------------- manifest

let manifest = readFileSync(MANIFEST, 'utf8');
manifest = manifest.replace(/^organization:.*\n/m, '');
manifest = manifest.replace(/^(name:.*\n)/m, `$1organization: ${org.id}\n`);
writeFileSync(MANIFEST, manifest);
console.log(`  Manifest set to organization ${org.id}.`);

// ---------------------------------------------------------------- publish

const cli = process.platform === 'win32' ? 'npx.cmd' : 'npx';
const run = (args) =>
    execFileSync(cli, args, { cwd: HERE, stdio: 'inherit', env: { ...process.env, GITBOOK_TOKEN: token } });

console.log('\n  Authenticating the CLI...');
run(['--yes', '@gitbook/cli', 'auth', '-t', token]);

console.log('  Publishing...\n');
run(['--yes', '@gitbook/cli', 'publish', '.']);

console.log(`
  Published.

  Last step, in the browser:
    1. Open  https://app.gitbook.com/o/${org.id}/integrations
    2. Find "Annotated Slides" and click Install
    3. Choose the space for this site

  Then the talk page renders the deck inline — one slide, Prev and Next
  buttons, narration underneath.
`);

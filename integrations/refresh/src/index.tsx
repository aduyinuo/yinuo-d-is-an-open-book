import { createIntegration, createComponent } from '@gitbook/runtime';

/**
 * A button on the page that starts a GitHub Actions workflow.
 *
 * GitBook renders markdown and runs no scripts, so nothing written into a page
 * can start anything. A ContentKit button can, because the press is handled
 * here — on the integration's own runtime — rather than in the reader's
 * browser. That is what makes this possible at all.
 */

type Props = {
    /** Which workflow file to dispatch. */
    workflow?: string;
    /** What the button says. */
    label?: string;
};

/** The only action this block dispatches. */
type Action = { action: 'run' };

type State = {
    workflow: string;
    label: string;
    /** What happened last time the button was pressed. */
    message: string;
    ok: boolean;
};

const WORKFLOWS: Record<string, string> = {
    board: 'activity.yml',
    opportunities: 'opportunities.yml',
};

const DEFAULT_REPO = 'aduyinuo/yinuo-d-is-an-open-book';

function fileFor(workflow: string): string {
    return WORKFLOWS[workflow] || (workflow.endsWith('.yml') ? workflow : 'activity.yml');
}

function labelFor(workflow: string): string {
    return workflow === 'opportunities' ? 'Find opportunities now' : 'Refresh the board now';
}

async function dispatch(
    config: { token?: string; repo?: string; branch?: string },
    workflow: string,
): Promise<{ ok: boolean; message: string }> {
    const token = config.token;
    if (!token) {
        return {
            ok: false,
            message:
                'No GitHub token set. Open this integration’s configuration in the space and add one with Actions write access.',
        };
    }

    const repo = config.repo || DEFAULT_REPO;
    const branch = config.branch || 'main';
    const file = fileFor(workflow);

    let response: Response;
    try {
        response = await fetch(
            `https://api.github.com/repos/${repo}/actions/workflows/${file}/dispatches`,
            {
                method: 'POST',
                headers: {
                    Authorization: `Bearer ${token}`,
                    Accept: 'application/vnd.github+json',
                    'X-GitHub-Api-Version': '2022-11-28',
                    'User-Agent': 'openbook-refresh',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ ref: branch }),
            },
        );
    } catch (error) {
        return { ok: false, message: `Could not reach GitHub: ${String(error)}` };
    }

    if (response.status === 204) {
        return {
            ok: true,
            message:
                'Started. It takes a minute or two, and the page updates itself once the run finishes.',
        };
    }
    if (response.status === 404) {
        return {
            ok: false,
            message: `GitHub could not find ${file} on ${repo}. Check the workflow name and that the token can see the repository.`,
        };
    }
    if (response.status === 401 || response.status === 403) {
        return {
            ok: false,
            message: 'GitHub refused the token. It needs Actions: read and write on the repository.',
        };
    }
    const body = await response.text();
    return { ok: false, message: `GitHub said ${response.status}. ${body.slice(0, 160)}` };
}

const refreshBlock = createComponent<Props, State, Action>({
    componentId: 'refresh',

    initialState: (props) => {
        const workflow = props.workflow || 'board';
        return {
            workflow,
            label: props.label || labelFor(workflow),
            message: '',
            ok: false,
        };
    },

    async action(element, action, context) {
        if (action.action === 'run') {
            const config = (context.environment.spaceInstallation?.configuration ||
                {}) as { token?: string; repo?: string; branch?: string };
            const result = await dispatch(config, element.state.workflow);
            return {
                ...element,
                state: { ...element.state, message: result.message, ok: result.ok },
            };
        }
        return element;
    },

    async render(element) {
        const { label, message, ok } = element.state;
        return (
            <block>
                <card
                    title={label}
                    hint={
                        message ||
                        'Pulls the day’s logged time from Clockify and rebuilds the page.'
                    }
                    buttons={[
                        <button
                            label={message && ok ? 'Run again' : label}
                            style={message && !ok ? 'danger' : 'primary'}
                            tooltip="Starts the workflow on GitHub. Takes a minute or two."
                            onPress={{ action: 'run' }}
                        />,
                    ]}
                />
            </block>
        );
    },
});

export default createIntegration({
    components: [refreshBlock],
});

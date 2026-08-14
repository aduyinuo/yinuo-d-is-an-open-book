import { createIntegration, createComponent } from '@gitbook/runtime';

const BASE = 'https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides';

/** Accept either a full deck URL or a bare slug, and normalise to a URL. */
function deckUrl(props: { url?: string; deck?: string }): string | null {
    const { url, deck } = props;
    if (url && url.startsWith(BASE)) {
        return url.endsWith('.html') ? url : `${url}.html`;
    }
    if (deck) {
        const slug = deck.replace(/\.html$/, '').replace(/[^a-zA-Z0-9._-]/g, '');
        return slug ? `${BASE}/${slug}.html` : null;
    }
    return null;
}

const deckBlock = createComponent<
    { url?: string; deck?: string },
    { url?: string; deck?: string }
>({
    componentId: 'deck',
    initialState: (props) => ({ url: props.url, deck: props.deck }),

    // Fires when someone pastes a deck URL onto a page.
    async action(element, action) {
        switch (action.action) {
            case '@link.unfurl':
                return {
                    props: { url: (action as { url: string }).url },
                };
            default:
                return element;
        }
    },

    async render(element) {
        const src = deckUrl(element.props);

        if (!src) {
            return (
                <block>
                    <card
                        title="Annotated slides"
                        hint="Set the deck name, e.g. asu-brown-bag"
                    />
                </block>
            );
        }

        return (
            <block>
                <webframe
                    source={{ url: src }}
                    aspectRatio={4 / 3}
                    data={{}}
                />
            </block>
        );
    },
});

export default createIntegration({
    components: [deckBlock],
});

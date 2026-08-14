import { createIntegration, createComponent } from '@gitbook/runtime';

const BASE = 'https://aduyinuo.github.io/yinuo-d-is-an-open-book/slides';

const deck = createComponent<{ deck?: string; url?: string }>({
    componentId: 'deck',
    initialState: {},
    async action(element, action) {
        return element;
    },
    async render(element, context) {
        const { deck, url } = element.props;
        const src = url ?? `${BASE}/${deck}.html`;
        return (
            <block>
                <webframe
                    source={{ url: src }}
                    aspectRatio={16 / 9}
                />
            </block>
        );
    },
});

export default createIntegration({
    components: [deck],
});

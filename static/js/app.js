const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            isVisible: false,
            greeting: 'you clicked enter!',
            anyText: '',
        };
    },
    methods: {
        togglePanel() {
            this.isVisible = !this.isVisible
        },
        directRegister() {
            router.push({ path: '/register'})
        }
    },
})

app.mount('#app');
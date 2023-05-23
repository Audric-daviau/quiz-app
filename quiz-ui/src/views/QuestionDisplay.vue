<template>
    <div>
        <h2>{{ question.title }}</h2>
        <p>{{ question.description }}</p>
        <img v-if="question.image" :src="question.image" />
        <ul>
            <li v-for="option in question.options" :key="option.id" @click="selectOption(option)">
                {{ option.text }}
            </li>
        </ul>
        <a @click="selectOption(2)">La réponse D</a>
    </div>
</template>
  
<script>
export default {
    name: 'QuestionDisplay',
    props: {
        question: {
            type: Object,
        }
    },
    emits: ['answer-selected'], // Déclaration de l'événement émis
    methods: {
        selectOption(option) {
            this.$emit('answer-selected', option);
        }
    }
};
</script>
  
<style scoped>
/* Styles spécifiques au composant QuestionDisplay */
</style>
  
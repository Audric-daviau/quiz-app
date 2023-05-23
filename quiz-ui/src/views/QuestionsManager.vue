<template>
    <div v-if="currentQuestion">
        <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
        <QuestionDisplay :question="currentQuestion" @answer-selected="handleQuestionAnswered" />
        <button v-if="isLastQuestion" @click="endQuiz">End Quiz</button>
    </div>
</template>
  
<script>
import QuestionDisplay from './QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';

export default {
    name: 'QuestionsManager',
    components: {
        QuestionDisplay
    },
    data() {
        return {
            currentQuestionPosition: 1,
            totalNumberOfQuestions: 0,
            currentQuestion: {},
            quizFinished: false
        };
    },

    methods: {
        async loadQuestionByPosition(position) {
            const response = await QuizApiService.getQuestionByPosition(position);
            const resp = await QuizApiService.getQuizInfo()
            // console.log("response")
            console.log(response)
            if (response.status === 200) {
                this.currentQuestion = response.data;
                this.totalNumberOfQuestions = resp.data.size;
            }
        },
        handleQuestionAnswered(option) {
            // Handle question answered event
            console.log('Selected option:', option);
            this.$emit('answer-selected', 2);
            // Move to next question
            this.currentQuestionPosition++;
            if (this.currentQuestionPosition <= this.totalNumberOfQuestions) {
                this.loadQuestionByPosition(this.currentQuestionPosition);
            } else {
                this.endQuiz();
            }
        },
        endQuiz() {
            // Handle quiz end
            console.log('Quiz ended');
            this.quizFinished = true;
        },
    },
    created() {
        this.loadQuestionByPosition(this.currentQuestionPosition);
    },
    computed: {
        isLastQuestion() {
            return this.currentQuestionPosition === this.totalNumberOfQuestions;
        }
    }
};
</script>
  
<style scoped>
/* Styles spécifiques au composant QuestionsManager */
</style>  
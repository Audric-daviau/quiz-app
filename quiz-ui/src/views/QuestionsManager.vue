<template>
    <div class="content">
    <div v-if="currentQuestion" class="page">
        <h1>Question {{ currentQuestionPosition }} / {{ totalNumberOfQuestions }}</h1>
        <QuestionDisplay :question="currentQuestion" @answer-selected="handleQuestionAnswered" />
    </div>
    </div>
</template>
  
<script>
import QuestionDisplay from './QuestionDisplay.vue';
import QuizApiService from '@/services/QuizApiService';
import ParticipationStorageService from "@/services/ParticipationStorageService.js"

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
            quizFinished: false,
            selectedAnswers: [],
            participants: {
                playerName: '',
                answers: ''
            },
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
        handleQuestionAnswered(optionIndex) {
            // Handle question answered event
            optionIndex++;
            console.log('Selected optionIndex:', optionIndex);
            this.selectedAnswers.push(optionIndex); // Ajout de la réponse au tableau selectedAnswers

            // Enregistrement du tableau dans la session
            ParticipationStorageService.saveParticipationAnswers(this.selectedAnswers);

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
            this.quizFinished = true;
            this.$router.push({ name: 'your-score' });
            this.participants.playerName = ParticipationStorageService.getUsername();
            this.participants.answers = this.selectedAnswers;
            // Appel au service pour envoyer les informations au serveur
            QuizApiService.addParticipants(this.participants)
                .then(response => {
                    // Réponse du serveur
                    console.log('Participation saved:', response.data);
                    this.$router.push({ name: 'your-score' });
                })
                .catch(error => {
                    // Gestion de l'erreur
                    console.error('Error saving participation:', error);
                });
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
.header {
  text-align: left;
  margin-bottom: 20px;
}

h1{
    font-size: 1.5em;
    background-color: rgb(165, 8, 8);
    color:white;
    padding: 10px;
    border-radius: 10px;
    text-align: center;
}

.page { 
  color:black;
  font-size: 1em;
  background: url("../assets/quizDisplay.jpg") no-repeat center center fixed; 
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
}

</style>
<template>
  <div>
    <h1>Quiz</h1>
    <form @submit.prevent="submitForm">
      <div class="mb-3">
        <label for="username" class="form-label">Saisissez votre nom :</label>
        <input type="text" class="form-control" id="username" v-model="username">
        <p>{{ username }}</p>
      </div>
      <button class="btn btn-outline-danger mt-2" @click="launchNewQuiz">Go</button>
    </form>
  </div>
</template>
  
<script>
import ParticipationStorageService from "@/services/ParticipationStorageService.js"

export default {
  name: "NewQuizPage",
  data() {
    return {
      username: '',
    };
  },
  methods: {
    launchNewQuiz() {
      ParticipationStorageService.saveUsername(this.username);
      console.log("Launch new quiz with", this.username);
      this.$router.push('/questions'); // Redirection vers la page des questions
    },
  }
};
</script>
  
<style scoped>
.container {
  margin-top: 2rem;
}
</style>
<template>
  <div class = "page">
    <form @submit.prevent="submitForm">
      
    <h1>Quiz</h1>
      <div class="mb-3">
        <label for="username" class="form-label">Saisissez votre nom :</label>
        <input type="text" class="form-control" id="username" v-model="username">
        <p>{{ username }}</p>
      </div>
      <button class="btn btn-primary mt-2" @click="launchNewQuiz">Go</button>
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
  
<style scodped>
body {
    color: white;
    font-size: 2em;
    text-align: left;
}
form {
    display: inline-block;
}

.page { 
  background: url("../assets/NewQuizPage.jpg") no-repeat center center fixed; 
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
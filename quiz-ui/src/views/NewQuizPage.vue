<template>
  <div class = "page">
    <form @submit.prevent="submitForm">
      
    <h1>Quiz</h1>
      <div class="mb-3">
        <label for="username" class="form-label">Saisissez votre nom :</label>
        <input type="text" class="form-control" id="username" v-model="username">
        <p>{{ username }}</p>
      </div>
      <button @click="launchNewQuiz">Go</button>
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
h1 {
  font-size: 2.3em;
}
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
  font-size: 2em;
  align-items: center;
  justify-content: center;
}

button {
  background: transparent;
  color: white;
  border: none;  /* Remove default button border */
  border-radius: 12px;  /* Make corners rounded */
  padding: 10px 20px;  /* Add some padding */
  transition: background-color 0.3s ease;  /* Make hover effect transition smoothly */
  border: 2px solid black;
}

button:hover {
  background-color: rgba(0, 0, 0, 0.2);  /* Add a dark background on hover */
}
</style>
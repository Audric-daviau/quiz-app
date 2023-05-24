<template>
  <div class="home-page">
    <div class="content">
      <h1>LE ROI DU QUIZ CE SERA MOI !</h1>

      <div v-if="registeredScores.data && registeredScores.data.scores">
        <div v-for="scoreEntry in registeredScores.data.scores" :key="scoreEntry.date">
          {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
        </div>
      </div>

      <router-link to="/new-quiz">Go!</router-link>
    </div>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: {
        data: {
          scores: null,
        },
      },
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      // Appel au service pour récupérer les scores
      const scores = await quizApiService.getQuizInfo();
      this.registeredScores = scores; // Stockage des scores dans registeredScores
      console.log(this.registeredScores)
    } catch (error) {
      console.error("Erreur lors de la récupération des scores:", error);
    }
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 2rem;
}

div {
  margin: 2rem 0;
}

router-link {
  display: block;
  text-align: center;
}

.home-page {
  background-image: url("../assets/background_Home_Page.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content {
  text-align: center;
  padding: 2rem;
  background-color: rgba(255, 255, 255, 0.8);
  width: 100%;
  max-width: 600px; /* Adjust the value as needed */
  margin: 0 auto;
}
</style>
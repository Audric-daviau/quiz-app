<template>
  <h1>LE ROI DU QUIZ CE SERA MOI !</h1>

  <div v-if="registeredScores.data && registeredScores.data.scores">
    <div v-for="scoreEntry in registeredScores.data.scores" v-bind:key="scoreEntry.date">
      {{ scoreEntry.playerName }} - {{ scoreEntry.score }}
    </div>
  </div>

  <router-link to="/new-quiz">Go !</router-link>
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
  text-align: center; /* Added */
  margin-top: 2rem; /* Added */
}

div {
  margin: 2rem 0; /* Added */
}

router-link {
  display: block;
  text-align: center; /* Added */
}
</style>
<template>
  <h1>Home page</h1>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "HomePage",
  data() {
    return {
      registeredScores: [], // Variable tableau des scores
    };
  },
  async created() {
    console.log("Composant Home page 'created'");
    try {
      // Appel au service pour récupérer les scores
      const scores = await quizApiService.getScores();
      this.registeredScores = scores; // Stockage des scores dans registeredScores
    } catch (error) {
      console.error("Erreur lors de la récupération des scores:", error);
    }
  },
};
</script>
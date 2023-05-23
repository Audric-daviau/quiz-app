<template>
  <div>
    <h1>Votre Score</h1>
    <score-display :score="playerScore" :ranking="playerRanking" :best-scores="topScores" />
  </div>
</template>
  
<script>
import ScoreDisplay from "@/views/ScoreDisplay.vue";

export default {
  name: "YourScorePage",
  data() {
    return {
      playerScore: 100,
      playerRanking: 1,
      topScores: [
        { playerName: "John", score: 11 },
        { playerName: "Jane", score: 10 },
        { playerName: "Alice", score: 9 },
      ],
    };
  },
  components: {
    ScoreDisplay,
  },
};
</script>
  
<style scoped>
/* Styles spécifiques à la page */
</style>
  
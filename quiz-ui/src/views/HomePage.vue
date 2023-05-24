<template>
  <div class="home-page">
    <div class="content">
      <h1>LE ROI DU QUIZ CE SERA MOI !</h1>

      <div v-if="registeredScores.data && registeredScores.data.scores" class="score-chart">
        <div v-for="(scoreEntry, index) in registeredScores.data.scores" :key="scoreEntry.date" class="score-entry">
          <div class="player-rank">{{'# RANK ' + (index + 1 )}}</div>
          <div class="player-name">{{ scoreEntry.playerName }}</div>
          <div class="score">
            {{ scoreEntry.score > 1 ? scoreEntry.score + ' pts' : scoreEntry.score + ' pt' }}
          </div>
          <div class="score-date">{{ scoreEntry.date }}</div>
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
  background-color: rgba(141, 53, 58, 0.4);
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  margin-right: 45%;
}

.score-chart {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.score-entry {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #ccc;
}

.player-rank {
  font-weight: bold;
  font-size: 25px;
  margin-right: 6px;
  color: #142d69;
}

.player-name {
  font-size: 25px;
  font-weight: bold;
  padding: 6px;
  margin-right: 6px;
  color: #000000;
}

.score {
  color: #e30c0c;
  padding: 6px;
  font-size: 25px;
}

.score-date {
  padding: 8px;
  font-size: 24px;
  color: #1a5ccf;
  font-weight: 600;
}

@media (max-width: 600px) {
  .score-entry {
    flex-wrap: nowrap;
  }
}
</style>
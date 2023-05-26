<template>
  <div class="home-page">
    <div class="title-content">
      <h1>LE ROI DU QUIZ CE SERA MOI !</h1>
      <div class="content" v-if="registeredScores.data && registeredScores.data.scores">
        <div class="score-chart">
          <div class="score-container">
            <div v-for="(scoreEntry, index) in registeredScores.data.scores" :key="scoreEntry.date" class="score-entry">
              <div class="player-rank">{{ '# RANK ' + (index + 1) }}</div>
              <div class="player-name">{{ scoreEntry.playerName }}</div>
              <div class="score">{{ scoreEntry.score > 1 ? scoreEntry.score + ' pts' : scoreEntry.score + ' pt' }}</div>
              <div class="score-date">{{ scoreEntry.date }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <router-link class="go-button" to="/new-quiz">Gomu Gomu GO!</router-link>
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
    console.log("Component Home page 'created'");
    try {
      // Call the service to retrieve the scores
      const scores = await quizApiService.getQuizInfo();
      if (scores === undefined){
        this.registeredScores = scores; // Store the scores in registeredScores
      }else{
        this.registeredScores = {};
      }
      
      console.log(this.registeredScores);
    } catch (error) {
      console.error("Error retrieving scores:", error);
    }
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
  margin-top: 8%; /* Adjust the margin-top value as needed */
  font-size: 3rem;
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

.title-content {
  margin-top: 5%;
  margin-right: 5%;
}

.content {
  text-align: center;
  padding: 2rem;
  background-color: rgba(141, 53, 58, 0.4);
  width: 100%;
  max-width: 600px;
  margin: 0 auto;
  max-height: 100%;
  overflow: auto;
}

.score-container {
  max-height: 600px; /* Adjust the max height as needed */
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
  color: #f1c72e;
  padding: 6px;
  font-size: 25px;
}

.score-date {
  padding: 8px;
  font-size: 24px;
  color: #460808;
  font-weight: 600;
}

.go-button {
  margin-top: 10%;
  margin-right: 25%;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 240px;
  height: 80px;
  font-size: 24px;
  font-weight: bold;
  text-decoration: none;
  background-color: #ff5722;
  color: #ffffff;
  border-radius: 10px;
  transition: background-color 0.3s;
}

.go-button:hover {
  background-color: #ff784d;
}

@media (max-width: 600px) {
  .score-entry {
    flex-wrap: nowrap;
  }
}
</style>
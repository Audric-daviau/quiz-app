<template>
  <div class="page">
    <div class = form>
        <p>Score : {{ score }}</p>
        <p>Classement : {{ ranking }}</p>
        <p>Meilleurs scores</p>
        <ul>
            <li v-for="bestScore in bestScores" :key="bestScore.playerName">
                {{ bestScore.playerName }} - {{ bestScore.score }}
            </li>
        </ul>
        <button @click="retour">Retour</button>
    </div>
  </div>
</template>
  
<script>
import QuizApiService from '@/services/QuizApiService';
import ParticipationStorageService from "@/services/ParticipationStorageService.js"

export default {
    name: 'ScoreDisplay',
    data() {
      return {
        score: null,
        ranking: null,
        bestScores: []
      };
    },
    methods: {
      async getScore() {
        try {
          const playerName = ParticipationStorageService.getUsername()
          const response = await QuizApiService.getScoreParticipant(playerName);
          this.score = response.data.score[0];
        } catch (error) {
          console.error(error);
        }
      },
      retour() {
        this.$router.push('/');
      },
      async getClassParticipant(){
        try {
          const response = await QuizApiService.getClassParticipant();
          console.log(response)
          this.bestScores = response.data.scores;
        } catch (error) {
          console.error(error);
        }
      },

      async getParticipantClass(){
        try {
          const playerName = ParticipationStorageService.getUsername()
          const response = await QuizApiService.getParticipantClass(playerName);
          console.log(response)
          this.ranking = response.data.classe;
        } catch (error) {
          console.error(error);
        }
      }
    },
    created() {
      this.getScore();
      this.getClassParticipant()
      this.getParticipantClass()
    }
};
</script>
  
<style scoped>
.page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.content {
  text-align: center;
}

h1 {
  font-size: 2em;
  margin-bottom: 20px;
}

h2 {
  font-size: 2.5em;
}

.pts {
  display: flex;
  flex-wrap: wrap;
}

ul li {
  list-style: none;
  flex: 0 0 50%; /* Each item occupies 50% of the container width */
  padding: 10px;
}

ul li:before {
  content: '👒';
}
</style>
  
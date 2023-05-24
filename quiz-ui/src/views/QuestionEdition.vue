<template>
  <div id="question-edit">
    <h2>Édition de Question</h2>

    <form>
      <div class="form-group">
        <label for="position">Position</label>
        <input id="position" type="number" v-model="question.position" />
      </div>

      <div class="form-group">
        <label for="title">Titre</label>
        <input id="title" type="text" v-model="question.title" />
      </div>

      <div class="form-group">
        <label for="text">Intitulé</label>
        <input id="text" type="text" v-model="question.text"/>
      </div>

      <div class="form-group">
        <label for="image">Image</label>
        <ImageUpload @file-change="imageFileChangedHandler" />
        <img v-if="question.image" :src="question.image" />
        
      </div>

      <div class="form-group" v-for="(answer, index) in question.possibleAnswers" :key="index">
        <label :for="'answer' + index">Intitulé de la réponse</label>
        <input :id="'answer' + index" v-model="answer.text" type="text"/>

        <input type="checkbox" v-model="answer.isCorrect" />
        <label :for="'answer' + index">Réponse correcte</label>
      </div>

      <div class="form-group">
        <button @click.prevent="saveQuestion">Sauvegarder</button>
        <button @click="cancel">Annuler</button>
      </div>
    </form>
  </div>
</template>
<script>
import quizApiService from "@/services/QuizApiService";
import ImageUpload from './ImageUpload.vue';

export default {
    name: "QuestionEdition",
    components: {
      ImageUpload
    },
    data() {
      return {
        question: {
          position: '',
          title: '',
          text: '',
          image: '',
          possibleAnswers: [
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
            { text: '', isCorrect: false },
          ],
        },
      };
    },
    methods: {
      async fetchQuestion() {
        const questionId = this.$route.params.questionId;
        if (questionId) {
      try {
        const response = await quizApiService.getQuestionById(questionId);
        this.question = response.data;
      } catch (error) {
        console.error(error);
      }
    } else {
      this.question = {
        position: '',
        title: '',
        text: '',
        image: '',
        possibleAnswers: [
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
          { text: '', isCorrect: false },
        ],
      };
    }
      },
      
      async saveQuestion() {
        
        const questionId = this.$route.params.questionId;
          const token = localStorage.getItem('token');
          if(questionId) {
            try {
              const response = await quizApiService.updateQuestionById(questionId, this.question);
              console.log(response);
              this.$router.push('/questionsList');
            } catch (error) {
              console.error(error);
            }
          } else {
            try {
              const response = await quizApiService.addQuestion(this.question);
              console.log(response);
              this.$router.push('/questionsList');
            } catch (error) {
              console.error(error);
            }
          }
        },
    cancel() {
      this.$router.push('/questionsList');
    },
    imageFileChangedHandler(b64String) {
      console.log(b64String);
      this.question.image = b64String;
    }
    },
    mounted() {
      this.fetchQuestion();
    },
}
</script>
<style scoped>
h2 {
  font-size: 2em;
  margin-top: 50px;
}
#question-edit {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: left;
  height: 100vh; /* full viewport height */
}

.form-group {
  display: flex;
  flex-direction: row;
  gap: 10px;
  align-items: center;
}

.form-group label {
  flex-basis: 150px; /* Ajustez la valeur en fonction de la largeur souhaitée pour les labels */
}

.form-group input[type="text"],
.form-group input[type="number"] {
  flex-grow: 1;
}

.form-group input[type="checkbox"] {
  margin-right: 10px; /* Espacement entre la case à cocher et l'intitulé de réponse */
}
</style>


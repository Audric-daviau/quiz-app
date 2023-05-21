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
        <input id="image" @change="onFileChange" type="file" accept="image/*" />
        <img v-if="question.image" :src="question.image" />
      </div>

      <div class="form-group" v-for="(answer, index) in question.answers" :key="index">
        <label :for="'answer' + index">Intitulé de la réponse</label>
        <input :id="'answer' + index" v-model="answer.text" type="text" required />

        <input type="checkbox" v-model="answer.isCorrect" />
        <label :for="'answer' + index">Réponse correcte</label>
      </div>

      <div class="form-group">
        <button type="submit">Sauvegarder</button>
        <button @click.prevent="cancel">Annuler</button>
      </div>
    </form>
  </div>
</template>
<script>
import quizApiService from "@/services/QuizApiService";

export default {
    name: "QuestionEdition",
    data() {
      return {
        question: {
          position: '',
          title: '',
          text: '',
          image: '',
          answers: [
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
        try {
          const response = await quizApiService.getQuestionById(questionId);
          this.question = response.data;
        } catch (error) {
          console.error(error);
        }
      },
    },
    createImage(file) {
      // Implement your image handling logic here
      // For example, you can use FileReader API to read the image file
      // and convert it to a data URL
    },
    saveQuestion() {
      // Implement your saving logic here
      // Make sure to validate that only one answer is marked as correct
      this.$router.push('/questionsList');
    },
    cancel() {
      this.$router.push('/questionsList');
    },
    mounted() {
      this.fetchQuestion();
    },
}
</script>
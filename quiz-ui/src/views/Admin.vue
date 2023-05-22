<template>
  <div id="login">
    <h2>Admin Login</h2>

    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="password">Password</label>
        <input
          id="password"
          v-model="password"
          type="password"
          name="password"
          required
        />
      </div>

      <div class="form-group">
        <button type="submit">Connexion</button>
      </div>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>
    </form>
  </div>
</template>

<script>
import quizApiService from "@/services/QuizApiService";

export default {
  name: "Admin",
  data() {
    return {
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    submitForm() {
      // Implement your authentication logic here.
      quizApiService.login({password : this.password}).then(response => {
  if (response.status == 200) {
    window.localStorage.setItem("token", response.data.token);
    this.$router.push('/questionsList');
  }
}).catch(error => {
  if (error && error.response && error.response.status === 401) {
    this.errorMessage = 'Mauvais mot de passe';
  } else {
    console.log(error);
  }
});

    },
  },
};
</script>

<style scoped>
  #login {
    width: 300px;
    margin: 0 auto;
  }
  .form-group {
    margin-bottom: 15px;
  }
  .error-message {
    color: red;
  }
</style>
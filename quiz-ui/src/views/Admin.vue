<template>
  <div id="login" class="login-container">

    <form @submit.prevent="submitForm" class="login-form">
      
    <h2>Admin Login</h2>
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
      async submitForm() {
        try {
          const response = await quizApiService.login({ password: this.password });
  
          if (response.status === 200) {
            localStorage.setItem("token", response.data.token);
            this.$router.push('/questionsList');
          } else {
            this.errorMessage = 'Mauvais mot de passe';
          }
        } catch (error) {
          this.errorMessage = 'Mauvais mot de passe';
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
label {
  font-size: 1.5em;
  padding-right: 20px;
}

  .login-form {
    text-align: left;
  }
  .login-form h2 {
    font-size: 3em;
    margin-bottom: 20px;
}

.login-form .form-group {
    margin-bottom: 50px;
}
    .error-message {
      color: red;
    }
  </style>
  
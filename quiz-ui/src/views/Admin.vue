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
        // This is a placeholder logic to demonstrate the error message.
        if (this.password !== 'correct_password') {
          this.errorMessage = 'Mauvais mot de passe';
        } else {
          this.errorMessage = '';
          // Navigate to a different page or do something else on successful login
        }
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
  
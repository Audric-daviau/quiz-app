<template>
    <div>
      <button @click="$emit('logout')">Logout</button>
      <QuestionsList v-if="adminMode === 'QuestionsList'"/>
      <QuestionEdition v-else-if="adminMode === 'QuestionEdition'"/>
      <QuestionAdminDisplay v-else-if="adminMode === 'QuestionAdminDisplay'"/>
    </div>
  </template>
  
  <script>
  import QuestionsList from './QuestionsList.vue';
  import QuestionEdition from './QuestionEdition.vue';
  import QuestionAdminDisplay from './QuestionAdminDisplay.vue';
  
  export default {
    name: 'AdminPanel',
    props: ['adminMode'],
    components: {
      QuestionsList,
      QuestionEdition,
      QuestionAdminDisplay
    }
  };
  </script>  
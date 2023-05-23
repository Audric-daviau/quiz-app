<template>
    <div>
        <p>Score : {{ score }}</p>
        <p>Classement : {{ ranking }}</p>
        <p>Meilleurs scores :</p>
        <ul>
            <li v-for="bestScore in bestScores" :key="bestScore.playerName">
                {{ bestScore.playerName }} - {{ bestScore.score }}
            </li>
        </ul>
    </div>
</template>
  
<script>
export default {
    name: "ScoreDisplay",
    props: {
        score: {
            type: Number,
            required: true,
        },
        ranking: {
            type: Number,
            required: true,
        },
        bestScores: {
            type: Array,
            required: true,
        },
    },
};
</script>
  
<style scoped>
/* Styles spécifiques au composant */
</style>
  
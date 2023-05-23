export default {
  clear() {
    window.sessionStorage.clear();
  },
  saveUsername(username) {
    window.sessionStorage.setItem("username", username);
  },
  getUsername() {
    return window.sessionStorage.getItem("username");
  },
  saveParticipationScore(participationScore) {
    window.sessionStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    return window.sessionStorage.getItem("participationScore");
  },
  saveParticipationAnswers(answers) {
    window.sessionStorage.setItem("selectedAnswers", JSON.stringify(answers));
  },

  getParticipationAnswers() {
    const answersString = window.sessionStorage.getItem("selectedAnswers");
    return JSON.parse(answersString);
  },
};
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
  }
};
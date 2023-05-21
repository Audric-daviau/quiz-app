export default {
  clear() {
    window.localStorage.clear();
  },
  saveUsername(username) {
    window.localStorage.setItem("username", username);
  },
  getUsername() {
    return window.localStorage.getItem("username");
  },
  saveParticipationScore(participationScore) {
    window.localStorage.setItem("participationScore", participationScore);
  },
  getParticipationScore() {
    return window.localStorage.getItem("participationScore");
  }
};
import axios from "axios";

const instance = axios.create({
	baseURL: `${import.meta.env.VITE_API_URL}`,
  json: true
});

export default {
  async call(method, resource, data = null, token = null, params) {
    var headers = {
      "Content-Type": "application/json",
    };
    if (token != null) {
      headers.authorization = "Bearer " + token;
    }

    return instance({
      method,
      headers: headers,
      url: resource,
      data,
      params
    })
      .then((response) => {
        return { status: response.status, data: response.data };
      })
      .catch((error) => {
        console.error(error);
      });
  },
  getQuizInfo() {
    return this.call("get", "quiz-info");
  },
  
  login(password){
    return this.call("post", "login", password)
  },

  getAllQuestions(){
    return this.call("get", "questions/all")
  },

  getQuestionById(questionId){
    return this.call("get", `questions/${questionId}`)
  },

  getQuestionByPosition(position){
    return this.call("get", `questions`, null, null, {position});
  },

  addQuestion(question){
    const token = localStorage.getItem('token'); // assuming you have the token stored in localStorage
    const headers = { 
        Authorization: `Bearer ${token}` 
    };
    return this.call("post", "questions", question, headers)
  },

  updateQuestionById(questionId, question){
    const token = localStorage.getItem('token'); // assuming you have the token stored in localStorage
    const headers = { 
        Authorization: `Bearer ${token}` 
    };
    return this.call("put", `questions/${questionId}`, question, headers)
  },

  deleteQuestionById(questionId){
    const token = localStorage.getItem('token'); // assuming you have the token stored in localStorage
    const headers = { 
      Authorization: `Bearer ${token}` 
    };
    return this.call("delete", `questions/${questionId}`, null, headers)
  },

  getScoreParticipant(playerName){
    return this.call("get",  "participations/all", null, null, {playerName})
  },

  getClassParticipant(){
    return this.call("get", "participations")
  },

  getParticipantClass(playerName){
    return this.call("get",  "participations/classement", null, null, {playerName})
  },

  addParticipants(participant){
    return this.call("post", "/participations", participant)
  }
};
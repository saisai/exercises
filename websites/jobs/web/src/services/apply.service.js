import http from "../http-common";

class ApplyService {
    getAll() {
      return http.get("/apply");
    }
  
    get(id) {
      return http.get(`/apply/${id}`);
    }
  
    create(data) {
      return http.post("/apply", data);
    }
  
    update(id, data) {
      return http.put(`/apply/${id}`, data);
    }
  
    delete(id) {
      return http.delete(`/apply/${id}`);
    }
  
    deleteAll() {
      return http.delete(`/apply`);
    }
  
    findByTitle(title) {
      return http.get(`/apply?title=${title}`);
    }
  }
  
  export default new ApplyService();
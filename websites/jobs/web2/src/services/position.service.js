import http from "../http-common";

class PositionService {
    getAll() {
      return http.get("/position");
    }
  
    get(id) {
      return http.get(`/position/${id}`);
    }
  
    create(data) {
      return http.post("/position", data);
    }
  
    update(id, data) {
      return http.put(`/position/${id}`, data);
    }
  
    delete(id) {
      return http.delete(`/position/${id}`);
    }
  
    deleteAll() {
      return http.delete(`/position`);
    }
  
    findByTitle(title) {
      return http.get(`/apply?title=${title}`);
    }
  }
  
  export default new PositionService();
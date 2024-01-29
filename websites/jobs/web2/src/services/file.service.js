import axios from "axios";

import http from "../http-common";


const http2 = axios.create({
  baseURL: "http://localhost:8888/",
  headers: {
    "Content-type": "multipart/form-data",
  }
});

class FileService {
    getAll() {
      return http.get("/file");
    }
  
    get(id) {
      return http.get(`/file/${id}`);
    }
  
    create(data) {
      return http2.post("/file", data);
    }
  
    update(id, data) {
      return http.put(`/file/${id}`, data);
    }
  
    delete(id) {
      return http.delete(`/file/${id}`);
    }
  
    deleteAll() {
      return http.delete(`/file`);
    }
  
    findByTitle(title) {
      return http.get(`/apply?title=${title}`);
    }
  }
  
  export default new FileService();
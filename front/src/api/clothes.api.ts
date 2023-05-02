import axios from "axios";

const clothesApi = axios.create({
  baseURL: "http://localhost:8000/prendas/api/prenda/",
});

export const getAllClothes = () => clothesApi.get("/");

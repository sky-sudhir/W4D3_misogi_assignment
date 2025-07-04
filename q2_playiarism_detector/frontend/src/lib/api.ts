import axios from 'axios';
import Cookies from 'js-cookie';

const API_BASE_URL = 'http://localhost:8000';

// Create axios instance
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = Cookies.get('auth_token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Handle token expiration
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      Cookies.remove('auth_token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Types
export interface Product {
  id: number;
  name: string;
  category: string;
  subcategory: string;
  price: number;
  description: string;
  rating: number;
  reviews_count: number;
  brand: string;
  features: string[];
  image_url: string;
}

export interface User {
  id: number;
  username: string;
  email: string;
}

export interface UserProfile {
  user: User;
  interactions_count: number;
  preferences: Array<{
    category: string;
    score: number;
  }>;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface RecommendationResponse {
  recommendations: Product[];
}

// Authentication API
export const authAPI = {
  register: async (username: string, email: string, password: string): Promise<AuthResponse> => {
    const response = await api.post('/register', { username, email, password });
    return response.data;
  },

  login: async (username: string, password: string): Promise<AuthResponse> => {
    const response = await api.post('/login', { username, password });
    return response.data;
  },

  logout: () => {
    Cookies.remove('auth_token');
  },

  isAuthenticated: (): boolean => {
    return !!Cookies.get('auth_token');
  },

  setToken: (token: string) => {
    Cookies.set('auth_token', token, { expires: 1 }); // 1 day
  },
};

// Products API
export const productsAPI = {
  getProducts: async (category?: string, search?: string): Promise<Product[]> => {
    const params = new URLSearchParams();
    if (category) params.append('category', category);
    if (search) params.append('search', search);
    
    const response = await api.get(`/products?${params.toString()}`);
    return response.data;
  },

  getProduct: async (productId: number): Promise<Product> => {
    const response = await api.get(`/products/${productId}`);
    return response.data;
  },

  getCategories: async (): Promise<string[]> => {
    const response = await api.get('/categories');
    return response.data.categories;
  },
};

// Interactions API
export const interactionsAPI = {
  recordInteraction: async (
    productId: number,
    interactionType: 'view' | 'like' | 'purchase' | 'rating',
    rating?: number
  ) => {
    const response = await api.post('/interactions', {
      product_id: productId,
      interaction_type: interactionType,
      rating,
    });
    return response.data;
  },
};

// Recommendations API
export const recommendationsAPI = {
  getPopular: async (limit: number = 10): Promise<RecommendationResponse> => {
    const response = await api.get(`/recommendations/popular?limit=${limit}`);
    return response.data;
  },

  getContentBased: async (productId: number, limit: number = 5): Promise<RecommendationResponse> => {
    const response = await api.get(`/recommendations/content/${productId}?limit=${limit}`);
    return response.data;
  },

  getCollaborative: async (limit: number = 5): Promise<RecommendationResponse> => {
    const response = await api.get(`/recommendations/collaborative?limit=${limit}`);
    return response.data;
  },

  getByCategory: async (category: string, limit: number = 5): Promise<RecommendationResponse> => {
    const response = await api.get(`/recommendations/category/${category}?limit=${limit}`);
    return response.data;
  },

  getPersonalized: async (limit: number = 10): Promise<RecommendationResponse> => {
    const response = await api.get(`/recommendations/personalized?limit=${limit}`);
    return response.data;
  },
};

// User API
export const userAPI = {
  getProfile: async (): Promise<UserProfile> => {
    const response = await api.get('/user/profile');
    return response.data;
  },
};

export default api; 
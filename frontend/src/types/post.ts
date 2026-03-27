export interface Post {
  id: number;
  image: string;
  videoUrl?: string;
  stats: string[];
  desc: string;
  username?: string;
  followers?: string;
  likes?: string;
  comments?: string;
  date?: string;
}

export interface BackendPost {
  id: string;
  user_id: string;
  title: string;
  text: string;
  created_at: string;
  updated_at: string;
}

export interface MyPostsResponse {
  items: BackendPost[];
  total: number;
  skip: number;
  limit: number;
}


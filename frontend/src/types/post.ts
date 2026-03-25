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


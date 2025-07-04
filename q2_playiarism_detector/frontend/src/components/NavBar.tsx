"use client";
import Link from "next/link";
import { usePathname, useRouter } from "next/navigation";
import { useState, useEffect } from "react";
import { Button } from "./ui/button";
import { User, LogOut, ShoppingBag, Heart, TrendingUp } from "lucide-react";
import { authAPI, userAPI, UserProfile } from "../lib/api";

export function NavBar() {
  const pathname = usePathname();
  const router = useRouter();
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [userProfile, setUserProfile] = useState<UserProfile | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkAuth = async () => {
      const authenticated = authAPI.isAuthenticated();
      setIsAuthenticated(authenticated);
      
      if (authenticated) {
        try {
          const profile = await userAPI.getProfile();
          setUserProfile(profile);
        } catch (error) {
          console.error('Failed to fetch user profile:', error);
          // Token might be expired
          authAPI.logout();
          setIsAuthenticated(false);
        }
      }
      setLoading(false);
    };

    checkAuth();
  }, []);

  const handleLogout = () => {
    authAPI.logout();
    setIsAuthenticated(false);
    setUserProfile(null);
    router.push('/');
  };

  const navItems = [
    { name: "Home", path: "/", icon: ShoppingBag },
    { name: "Products", path: "/products", icon: ShoppingBag },
    { name: "Recommendations", path: "/recommendations", icon: TrendingUp },
  ];

  const authenticatedNavItems = [
    { name: "Wishlist", path: "/wishlist", icon: Heart },
    { name: "Profile", path: "/profile", icon: User },
  ];

  return (
    <header className="border-b bg-white shadow-sm">
      <div className="container mx-auto px-4 py-4">
        <nav className="flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold text-blue-600 hover:text-blue-700 transition-colors">
            🛍️ RecommendMe
          </Link>
          
          <div className="hidden md:flex items-center space-x-6">
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <Link
                  key={item.path}
                  href={item.path}
                  className={`flex items-center space-x-1 text-sm font-medium transition-colors hover:text-blue-600 ${
                    pathname === item.path ? "text-blue-600" : "text-gray-600"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
            
            {isAuthenticated && authenticatedNavItems.map((item) => {
              const Icon = item.icon;
              return (
                <Link
                  key={item.path}
                  href={item.path}
                  className={`flex items-center space-x-1 text-sm font-medium transition-colors hover:text-blue-600 ${
                    pathname === item.path ? "text-blue-600" : "text-gray-600"
                  }`}
                >
                  <Icon className="w-4 h-4" />
                  <span>{item.name}</span>
                </Link>
              );
            })}
          </div>

          <div className="flex items-center space-x-4">
            {loading ? (
              <div className="w-8 h-8 bg-gray-200 rounded-full animate-pulse"></div>
            ) : isAuthenticated && userProfile ? (
              <div className="flex items-center space-x-3">
                <div className="text-right">
                  <p className="text-sm font-medium text-gray-900">
                    {userProfile.user.username}
                  </p>
                  <p className="text-xs text-gray-500">
                    {userProfile.interactions_count} interactions
                  </p>
                </div>
                <Button
                  variant="outline"
                  size="sm"
                  onClick={handleLogout}
                  className="flex items-center space-x-1"
                >
                  <LogOut className="w-4 h-4" />
                  <span>Logout</span>
                </Button>
              </div>
            ) : (
              <div className="flex items-center space-x-2">
                <Button
                  variant="ghost"
                  size="sm"
                  onClick={() => router.push('/auth')}
                >
                  Sign In
                </Button>
                <Button
                  size="sm"
                  onClick={() => router.push('/auth')}
                >
                  Get Started
                </Button>
              </div>
            )}
          </div>
        </nav>

        {/* Mobile Navigation */}
        <div className="md:hidden mt-4 flex items-center justify-center space-x-4 overflow-x-auto">
          {navItems.map((item) => {
            const Icon = item.icon;
            return (
              <Link
                key={item.path}
                href={item.path}
                className={`flex flex-col items-center space-y-1 px-3 py-2 rounded-lg transition-colors ${
                  pathname === item.path 
                    ? "bg-blue-100 text-blue-600" 
                    : "text-gray-600 hover:bg-gray-100"
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="text-xs font-medium whitespace-nowrap">{item.name}</span>
              </Link>
            );
          })}
          
          {isAuthenticated && authenticatedNavItems.map((item) => {
            const Icon = item.icon;
            return (
              <Link
                key={item.path}
                href={item.path}
                className={`flex flex-col items-center space-y-1 px-3 py-2 rounded-lg transition-colors ${
                  pathname === item.path 
                    ? "bg-blue-100 text-blue-600" 
                    : "text-gray-600 hover:bg-gray-100"
                }`}
              >
                <Icon className="w-5 h-5" />
                <span className="text-xs font-medium whitespace-nowrap">{item.name}</span>
              </Link>
            );
          })}
        </div>
      </div>
    </header>
  );
}

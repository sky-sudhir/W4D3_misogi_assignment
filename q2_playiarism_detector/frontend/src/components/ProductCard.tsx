"use client";

import { useState } from 'react';
import { Card } from './ui/card';
import { Button } from './ui/button';
import { Heart, ShoppingCart, Eye, Star } from 'lucide-react';
import { Product, interactionsAPI, authAPI } from '../lib/api';

interface ProductCardProps {
  product: Product;
  onProductClick?: (product: Product) => void;
  showRecommendations?: boolean;
}

export function ProductCard({ product, onProductClick, showRecommendations = false }: ProductCardProps) {
  const [liked, setLiked] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleInteraction = async (type: 'view' | 'like' | 'purchase') => {
    if (!authAPI.isAuthenticated()) {
      // Redirect to login or show login modal
      return;
    }

    setLoading(true);
    try {
      await interactionsAPI.recordInteraction(product.id, type);
      if (type === 'like') {
        setLiked(!liked);
      }
    } catch (error) {
      console.error('Failed to record interaction:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCardClick = () => {
    handleInteraction('view');
    if (onProductClick) {
      onProductClick(product);
    }
  };

  const formatPrice = (price: number) => {
    return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
    }).format(price);
  };

  const renderStars = (rating: number) => {
    const stars = [];
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;

    for (let i = 0; i < fullStars; i++) {
      stars.push(
        <Star key={i} className="w-4 h-4 fill-yellow-400 text-yellow-400" />
      );
    }

    if (hasHalfStar) {
      stars.push(
        <Star key="half" className="w-4 h-4 fill-yellow-400 text-yellow-400 opacity-50" />
      );
    }

    const emptyStars = 5 - Math.ceil(rating);
    for (let i = 0; i < emptyStars; i++) {
      stars.push(
        <Star key={`empty-${i}`} className="w-4 h-4 text-gray-300" />
      );
    }

    return stars;
  };

  return (
    <Card className="group cursor-pointer transition-all duration-300 hover:shadow-lg hover:scale-105">
      <div onClick={handleCardClick} className="p-4">
        {/* Product Image Placeholder */}
        <div className="aspect-square bg-gray-100 rounded-lg mb-4 flex items-center justify-center overflow-hidden">
          <div className="text-gray-400 text-center">
            <div className="text-4xl mb-2">📦</div>
            <div className="text-xs">Product Image</div>
          </div>
        </div>

        {/* Product Info */}
        <div className="space-y-2">
          <div className="flex items-start justify-between">
            <h3 className="font-semibold text-lg line-clamp-2 group-hover:text-blue-600 transition-colors">
              {product.name}
            </h3>
            <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full whitespace-nowrap ml-2">
              {product.category}
            </span>
          </div>

          <p className="text-sm text-gray-600 line-clamp-2">
            {product.description}
          </p>

          <div className="flex items-center space-x-2">
            <div className="flex items-center">
              {renderStars(product.rating)}
            </div>
            <span className="text-sm text-gray-500">
              {product.rating} ({product.reviews_count} reviews)
            </span>
          </div>

          <div className="flex items-center justify-between">
            <span className="text-xl font-bold text-green-600">
              {formatPrice(product.price)}
            </span>
            <span className="text-sm text-gray-500">
              {product.brand}
            </span>
          </div>

          {/* Features */}
          <div className="flex flex-wrap gap-1">
            {product.features.slice(0, 3).map((feature, index) => (
              <span
                key={index}
                className="text-xs bg-gray-100 text-gray-700 px-2 py-1 rounded"
              >
                {feature}
              </span>
            ))}
            {product.features.length > 3 && (
              <span className="text-xs text-gray-500">
                +{product.features.length - 3} more
              </span>
            )}
          </div>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="px-4 pb-4 flex space-x-2">
        <Button
          variant="outline"
          size="sm"
          onClick={(e) => {
            e.stopPropagation();
            handleInteraction('like');
          }}
          disabled={loading}
          className={`flex-1 ${liked ? 'bg-red-50 text-red-600 border-red-200' : ''}`}
        >
          <Heart className={`w-4 h-4 mr-2 ${liked ? 'fill-current' : ''}`} />
          {liked ? 'Liked' : 'Like'}
        </Button>

        <Button
          size="sm"
          onClick={(e) => {
            e.stopPropagation();
            handleInteraction('purchase');
          }}
          disabled={loading}
          className="flex-1"
        >
          <ShoppingCart className="w-4 h-4 mr-2" />
          Buy Now
        </Button>
      </div>

      {showRecommendations && (
        <div className="px-4 pb-4">
          <Button
            variant="ghost"
            size="sm"
            className="w-full text-blue-600 hover:text-blue-800"
            onClick={(e) => {
              e.stopPropagation();
              // Handle show recommendations
            }}
          >
            <Eye className="w-4 h-4 mr-2" />
            View Similar Products
          </Button>
        </div>
      )}
    </Card>
  );
} 
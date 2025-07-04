"use client";

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { AuthForm } from '../../components/AuthForm';

export default function AuthPage() {
  const [mode, setMode] = useState<'login' | 'register'>('login');
  const router = useRouter();

  const handleSuccess = () => {
    router.push('/');
  };

  const toggleMode = () => {
    setMode(mode === 'login' ? 'register' : 'login');
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center py-12 px-4">
      <AuthForm
        mode={mode}
        onSuccess={handleSuccess}
        onToggleMode={toggleMode}
      />
    </div>
  );
} 
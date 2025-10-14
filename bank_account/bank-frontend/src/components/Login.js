import React, { useState } from "react";
import {
  Input,
  Button,
  VStack,
  useToast,
  Heading,
  Box,
  FormControl,
  FormLabel,
} from "@chakra-ui/react";
import api from "../api";

export default function Login({ onLogin }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleLogin = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);

    try {
      const res = await api.login({ email, password });
      toast({ title: "Login successful!", status: "success", duration: 3000, isClosable: true });
      onLogin(res.data); 
    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Login failed";
      toast({ title: "Login failed", description: msg, status: "error", duration: 4000, isClosable: true });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>Login</Heading>
      <VStack spacing={3}>
        <FormControl>
          <FormLabel>Email</FormLabel>
          <Input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Enter email" />
        </FormControl>
        <FormControl>
          <FormLabel>Password</FormLabel>
          <Input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter password" />
        </FormControl>
        <Button colorScheme="blue" onClick={handleLogin} w="full" isLoading={isSubmitting}>
          Login
        </Button>
      </VStack>
    </Box>
  );
}

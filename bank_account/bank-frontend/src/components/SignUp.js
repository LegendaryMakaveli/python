
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

export default function Signup({ onSignup }) {
  const [form, setForm] = useState({ email: "", password: "", name: "" });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleSignup = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);

    try {
      const res = await api.signup(form);
      toast({ title: "Signup successful!", status: "success", duration: 3000, isClosable: true });
      onSignup(res.data); 
    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Signup failed";
      toast({ title: "Signup failed", description: msg, status: "error", duration: 4000, isClosable: true });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>Sign Up</Heading>
      <VStack spacing={3}>
        <FormControl>
          <FormLabel>Name</FormLabel>
          <Input value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} placeholder="Full name" />
        </FormControl>
        <FormControl>
          <FormLabel>Email</FormLabel>
          <Input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} placeholder="Email" />
        </FormControl>
        <FormControl>
          <FormLabel>Password</FormLabel>
          <Input type="password" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} placeholder="Password" />
        </FormControl>
        <Button colorScheme="green" onClick={handleSignup} w="full" isLoading={isSubmitting}>
          Sign Up
        </Button>
      </VStack>
    </Box>
  );
}

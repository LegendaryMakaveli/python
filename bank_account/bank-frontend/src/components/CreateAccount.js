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

export default function CreateAccount({ refreshAccounts }) {
  const [form, setForm] = useState({
    first_name: "", last_name: "", address: "", email: "", phone_number: "", nin: "", bvn: ""
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleCreate = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      await api.createAccount(form);
      toast({ title: "Account created!", status: "success", duration: 3000, isClosable: true });
      setForm({ first_name: "", last_name: "", address: "", email: "", phone_number: "", nin: "", bvn: "" });
      refreshAccounts?.();
    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Error";
      toast({ title: "Account creation failed", description: msg, status: "error", duration: 4000, isClosable: true });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>Create Account</Heading>
      <VStack spacing={3}>
        {["first_name","last_name","address","email","phone_number","nin","bvn"].map((key) => (
          <FormControl key={key}>
            <FormLabel textTransform="capitalize">{key.replace("_", " ")}</FormLabel>
            <Input placeholder={key.replace("_"," ")} value={form[key]} onChange={(e) => setForm({ ...form, [key]: e.target.value })} />
          </FormControl>
        ))}
        <Button type="button" colorScheme="teal" onClick={handleCreate} w="full" isLoading={isSubmitting}>Create Account</Button>
      </VStack>
    </Box>
  );
}

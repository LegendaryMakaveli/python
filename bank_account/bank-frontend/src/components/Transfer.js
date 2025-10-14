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

export default function Transfer({ refreshAccounts }) {
  const [sender, setSender] = useState("");
  const [receiver, setReceiver] = useState("");
  const [amount, setAmount] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);
  const toast = useToast();

  const handleTransfer = async () => {
    if (isSubmitting) return;
    setIsSubmitting(true);
    try {
      await api.transfer(sender, receiver, parseFloat(amount));
      toast({ title: "Transfer successful!", status: "success", duration: 3000, isClosable: true });
      setSender("");
      setReceiver("");
      setAmount("");
      refreshAccounts?.();
    } catch (err) {
      const msg =
        typeof err.response?.data === "object"
          ? err.response?.data?.msg || JSON.stringify(err.response.data)
          : err.response?.data || "Error";
      toast({ title: "Transfer failed", description: msg, status: "error", duration: 4000, isClosable: true });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <Box p={5} borderWidth="1px" borderRadius="xl" boxShadow="md" bg="white">
      <Heading size="md" mb={4}>Transfer</Heading>
      <VStack spacing={3}>
        <FormControl>
          <FormLabel>Sender Account</FormLabel>
          <Input value={sender} onChange={(e) => setSender(e.target.value)} />
        </FormControl>
        <FormControl>
          <FormLabel>Receiver Account</FormLabel>
          <Input value={receiver} onChange={(e) => setReceiver(e.target.value)} />
        </FormControl>
        <FormControl>
          <FormLabel>Amount</FormLabel>
          <Input type="number" value={amount} onChange={(e) => setAmount(e.target.value)} />
        </FormControl>
        <Button type="button" colorScheme="orange" onClick={handleTransfer} w="full" isLoading={isSubmitting}>Transfer</Button>
      </VStack>
    </Box>
  );
}

import React, { useState } from "react";
import {
  Box,
  Button,
  Heading,
  Text,
  VStack,
  Flex,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalBody,
  ModalCloseButton,
  useDisclosure,
} from "@chakra-ui/react";
import { motion } from "framer-motion";
import Login from "./Login";
import SignUp from "./SignUp";

export default function LandingPage({ onLoginSuccess }) {
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [activeModal, setActiveModal] = useState(null);

  const openModal = (type) => {
    setActiveModal(type);
    onOpen();
  };

  return (
    <Box
      minH="100vh"
      bgImage="url('/your-background.jpg')" // Replace with your image path
      bgSize="cover"
      bgPosition="center"
      display="flex"
      flexDirection="column"
      alignItems="center"
      justifyContent="center"
    >
      <Box
        bg="rgba(255, 255, 255, 0.15)"
        p={10}
        rounded="2xl"
        shadow="2xl"
        backdropFilter="blur(20px)"
        textAlign="center"
        color="white"
      >
        <Heading mb={4} fontSize="4xl">
          🏦 Welcome to Makaveli Bank
        </Heading>
        <Text fontSize="xl" mb={8}>
          Secure, fast, and modern banking at your fingertips.
        </Text>
        <Flex gap={6} justify="center">
          <Button
            as={motion.button}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            colorScheme="blue"
            onClick={() => openModal("login")}
          >
            Login
          </Button>
          <Button
            as={motion.button}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            colorScheme="green"
            onClick={() => openModal("signup")}
          >
            Sign Up
          </Button>
        </Flex>
      </Box>

      <Modal isOpen={isOpen} onClose={onClose} isCentered>
        <ModalOverlay
          bg="rgba(0,0,0,0.4)"
          backdropFilter="blur(12px)"
        />
        <ModalContent>
          <ModalCloseButton />
          <ModalBody p={6}>
            {activeModal === "login" ? (
              <Login onLoginSuccess={onLoginSuccess} />
            ) : (
              <SignUp onSignUpSuccess={onLoginSuccess} />
            )}
          </ModalBody>
        </ModalContent>
      </Modal>
    </Box>
  );
}

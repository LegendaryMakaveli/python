import React, { useState, useEffect } from "react";
import {
  ChakraProvider,
  Box,
  Heading,
  SimpleGrid,
  Button,
  Modal,
  ModalOverlay,
  ModalContent,
  ModalHeader,
  ModalBody,
  ModalCloseButton,
  extendTheme,
  Flex,
} from "@chakra-ui/react";
import { motion, AnimatePresence } from "framer-motion";


import CreateAccount from "./components/CreateAccount";
import Deposit from "./components/Deposit";
import Withdraw from "./components/Withdraw";
import Transfer from "./components/Transfer";
import AccountList from "./components/AccountList";
import TransactionHistory from "./components/TransactionHistory";


import LandingPage from "./components/LandingPage";

const theme = extendTheme({
  colors: {
    brand: {
      blue: "#2B6CB0",
      green: "#2F855A",
      red: "#C53030",
      purple: "#6B46C1",
      yellow: "#D69E2E",
      orange: "#DD6B20",
    },
  },
});

const actions = [
  { key: "create", label: "Create Account", color: "blue" },
  { key: "deposit", label: "Deposit", color: "green" },
  { key: "withdraw", label: "Withdraw", color: "red" },
  { key: "transfer", label: "Transfer", color: "purple" },
  { key: "list", label: "Account List", color: "yellow" },
  { key: "history", label: "Transaction History", color: "orange" },
];

export default function App() {
  const [active, setActive] = useState("");
  const [user, setUser] = useState(null); 
  const closeModal = () => setActive("");


  useEffect(() => {
    const savedUser = localStorage.getItem("user");
    if (savedUser) {
      setUser(JSON.parse(savedUser));
    }
  }, []);


  useEffect(() => {
    if (user) {
      localStorage.setItem("user", JSON.stringify(user));
    } else {
      localStorage.removeItem("user");
    }
  }, [user]);


  const handleLogout = () => {
    setUser(null);
    setActive("");
  };


  const handleLoginSuccess = (loggedUser) => {
    setUser(loggedUser);
  };

  const renderContent = () => {
    switch (active) {
      case "create":
        return <CreateAccount />;
      case "deposit":
        return <Deposit />;
      case "withdraw":
        return <Withdraw />;
      case "transfer":
        return <Transfer />;
      case "list":
        return <AccountList />;
      case "history":
        return <TransactionHistory />;
      default:
        return null;
    }
  };

  const activeAction = actions.find((a) => a.key === active);


  if (!user) {
    return (
      <ChakraProvider theme={theme}>
        <LandingPage onLoginSuccess={handleLoginSuccess} />
      </ChakraProvider>
    );
  }


  return (
    <ChakraProvider theme={theme}>
      <Box
        minH="100vh"
        bgGradient="linear(to-br, teal.100, teal.300, blue.100)"
        display="flex"
        flexDirection="column"
        alignItems="center"
        justifyContent="center"
        p={6}
      >
        <Flex justify="space-between" w="100%" maxW="1200px" mb={6}>
          <Heading color="brand.blue" textShadow="0 2px 5px rgba(0,0,0,0.2)">
            🏦 Makaveli Bank Dashboard
          </Heading>
          <Button colorScheme="red" onClick={handleLogout}>
            Logout
          </Button>
        </Flex>

     
        <SimpleGrid columns={{ base: 1, sm: 2, md: 3 }} spacing={6}>
          {actions.map((action) => (
            <Button
              key={action.key}
              as={motion.button}
              whileHover={{ scale: 1.07 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => setActive(action.key)}
              bg={`brand.${action.color}`}
              color="white"
              size="lg"
              h="100px"
              w="200px"
              rounded="2xl"
              shadow="xl"
              fontWeight="bold"
              _hover={{ opacity: 0.9 }}
            >
              {action.label}
            </Button>
          ))}
        </SimpleGrid>

       
        <AnimatePresence>
          {active && (
            <Modal isOpen onClose={closeModal} isCentered size="xl" motionPreset="none">
              <ModalOverlay
                as={motion.div}
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
                bg="rgba(0, 0, 0, 0.4)"
                backdropFilter="blur(12px)"
                backdropBlur="12px"
              />
              <ModalContent
                as={motion.div}
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.8, opacity: 0 }}
                transition={{ duration: 0.3 }}
                bg={`rgba(255, 255, 255, 0.15)`}
                border="1px solid rgba(255, 255, 255, 0.3)"
                backdropFilter="blur(20px)"
                color="white"
                p={4}
                rounded="2xl"
                shadow="2xl"
                h="80vh"
              >
                <ModalHeader textAlign="center" fontSize="2xl">
                  {activeAction?.label}
                </ModalHeader>
                <ModalCloseButton color="white" />

                <ModalBody p={0}>
                  <Flex
                    align="center"
                    justify="center"
                    h="100%"
                    w="100%"
                    p={4}
                    as={motion.div}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 0.15, duration: 0.4 }}
                  >
                    <Box
                      bg="rgba(255, 255, 255, 0.9)"
                      color="gray.800"
                      p={6}
                      rounded="xl"
                      shadow="lg"
                      w="100%"
                      maxW="450px"
                    >
                      {renderContent()}
                    </Box>
                  </Flex>
                </ModalBody>
              </ModalContent>
            </Modal>
          )}
        </AnimatePresence>
      </Box>
    </ChakraProvider>
  );
}

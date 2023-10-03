import './App.css';
import {
    Input,
    Box,
    Container,
    Button,
    Flex,
    Heading,
    Text,
} from '@chakra-ui/react';

const data = [
    {
        title: 'Computer science',
        url: 'https://en.wikipedia.org/wiki/Computer_science',
        description:
            'Computer science is the study of computation, information, and automation.',
    },
    {
        title: 'Computer engineering',
        url: 'https://en.wikipedia.org/wiki/Computer_engineering',
        description:
            'Computer engineering is the study of computer science and electrical engineering. Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum. Lorem impsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum. Lorem impsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum. Lorem impsum dolor sit amet consectetur adipisicing elit. Quisquam, voluptatum.',
    },
];

function App() {
    return (
        <>
            <Box px={10} my={10}>
                <Container maxW="container.md">
                    <Heading as="h1" size="2xl" className="font-mono">
                        <span className="text-sky-500	">Wiki</span>
                        <span className="text-gray-400">Hunt</span>
                    </Heading>
                    <Flex gap={2}>
                        <Input />
                        <Button>Search</Button>
                    </Flex>
                    <Text className="text-sm text-gray-600" p={1}>
                        Se muestran {data.length} resultados
                    </Text>
                    <Box>
                        {data.map((item, index) => (
                            <Box
                                key={index}
                                my={2}
                                rounded="md"
                                shadow="lg"
                                p={3}
                            >
                                <Heading size="md">{item.title}</Heading>
                                <a
                                    href={item.url}
                                    target="_blank"
                                    rel="noreferrer"
                                    className="text-blue-400 text-sm"
                                >
                                    {item.url}
                                </a>
                                <Text className="truncate">
                                    {item.description}
                                </Text>
                            </Box>
                        ))}
                    </Box>
                </Container>
            </Box>
        </>
    );
}

export default App;

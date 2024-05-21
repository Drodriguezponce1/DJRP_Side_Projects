package Java.SocketPractice;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.*;
import java.util.*;

public class GreetServer {

    private ServerSocket serverSocket; // waits for requests to the host
    private Socket clientSocket; // simply a endpoint working on requests (client)

    private PrintWriter output; // simply a writer to write somewhere
    private BufferedReader input; // simply reads data

    public void start(int port) throws Exception
    {

        serverSocket = new ServerSocket(port);
        clientSocket = serverSocket.accept();
        output = new PrintWriter(clientSocket.getOutputStream(), true);
        input = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));

        String hello = input.readLine();

        if(hello.equals("Hello World"))
        {
            output.println("Hello Computer");
        }
        else{
            output.println("Unrecognized hello!");;
        }

    }

    public void stop() throws Exception
    {
        input.close();
        output.close();

        clientSocket.close();
        serverSocket.close();

    }

    public static void main(String[] args) {
        GreetServer g = new GreetServer();

        try {
            g.start(6666);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

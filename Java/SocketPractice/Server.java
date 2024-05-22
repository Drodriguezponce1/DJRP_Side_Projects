package Java.SocketPractice;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private ServerSocket server;
    private DataInputStream in;

    public static final int PORT = 3030;
    public static String stop_string = "CLOSE";

    public Server()
    {
        try{
            server = new ServerSocket(PORT);
            initConnection();
        }
        catch(IOException e)
        {
            e.printStackTrace();
        }
    }

    @SuppressWarnings("resource")
    public void initConnection() throws IOException
    {
        Socket s = server.accept();

        in = new DataInputStream(new BufferedInputStream(s.getInputStream()));
        readMessages();
        close();

    }

    public void close()
    {
        try {
            in.close();
            server.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }

    public void readMessages() throws IOException
    {
        String line = "";

        while(!line.equals(stop_string))
        {
            line = in.readUTF();
            System.out.println(line);


        }
        
    }

    public static void main(String[] args) {
        Server s = new Server();
    }
}

package Java.SocketPractice;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class Client {
    private Socket socket;
    private DataOutputStream out;
    private Scanner in;

    public Client()
    {
        try{
            socket = new Socket("localhost", 3030);
            out = new DataOutputStream(socket.getOutputStream());
            in = new Scanner(System.in);
            
            writeMessage();
        }
        catch(UnknownHostException e)
        {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

      
       
    }

    public void writeMessage() throws IOException
    {
        String line = "";

        while(!line.equals("CLOSE"))
        {
            line = in.nextLine();
            out.writeUTF(line);
        }
        close();
    }

    public void close() throws IOException
    {
        in.close();
        socket.close();
        in.close();
    }

    public static void main(String[] args) {
        Client c = new Client();
    }
}

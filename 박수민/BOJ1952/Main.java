import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int m = Integer.parseInt(st.nextToken());
		int n = Integer.parseInt(st.nextToken());
		
		boolean[][] visited = new boolean[m][n];
		int[] dx = {0,1,0,-1}; // 우, 하, 좌, 상
		int[] dy = {1,0,-1,0};
		int x = 0;	
		int y = 0;
		int dir = 0;	//방향
		int count = 0;
		visited[x][y] = true;
		
		for(int i = 0; i < m*n-1; i++) { // 이미 0,0은 방문했으니까 m*n-1까지
			int nx = x + dx[dir];	//예비 x,y
			int ny = y + dy[dir];
			
			if(nx >= 0 && nx < m && ny >= 0 && ny < n && !visited[nx][ny]) {	//x,y가 index를 벗어나지 않고 방문하지않은 인덱스일때
				x = nx;
				y = ny;
				visited[x][y] = true;
			} else {	// 안되는 거니까 방향을 바꿈
				dir = (dir+1)%4;	// %4인이유는 4가되면 자연스럽게 0이되어 순환할수 있도록 하기 위해
				count++;
				x += dx[dir];
				y += dy[dir];
				visited[x][y] = true;	
			}
		}
		
		System.out.println(count);
	}
}

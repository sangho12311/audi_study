import java.io.*;
import java.util.*;

class Solution
{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int test_case = Integer.parseInt(br.readLine()); // 테스트케이스 수 입력
		for(int t = 1; t <= test_case; t++) {	// 테스트케이스 for문
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			int[][] nums = new int[n][n];	// 파리 수 입력받을 2차원배열
			for(int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for(int j = 0; j < n; j++) {
					nums[i][j] = Integer.parseInt(st.nextToken()); // 파리 수 입력
				}
			}
			int max = 0;	//최댓값 max
			for(int i = 0; i <= n-m; i++) {	// 파리채크기에따라 인덱스벗어날수도 있으니 n-m인덱스까지만 체크
				for(int j = 0; j <= n-m; j++) {
					int sum = 0;	// 파리 수 저장할 변수
					for(int k = i; k < i +m; k++) {	// 현재 i,j인인덱스 기준으로 파리채 크기만큼 
						for(int l = j; l < j+m; l++) {
							sum += nums[k][l];	// 해당 인덱스 파리수 더해주기
						}
					}
					if(sum > max) max = sum;	// max보다 지금인덱스기준 파리채로 잡은 파리가 많으면 max를 바꿔줌
				}
			}
			System.out.println("#" + t + " " + max);
			
		}
	}
}

import java.util.Arrays;

/**
 * Created by mathe on 28/03/2018.
 */
public class Relogio {

    public static void main(String[] args) {

        Integer processo[] = {0, 1, 2, 3, 4, 5, 8,7,6,14,13,12,9,10,1,2,3,11,15};
        Integer paginas[][] = new Integer[8][2];
        int ponteiro = 0;
        int novo = 0;
        int crtl,ctrl2 = 0;
        boolean contem = false;


        for (int i = 0; i < processo.length; i++) {
            novo = processo[i];
            contem = false;
            for (int j = ponteiro; j < paginas.length; j++) {
                if (paginas[j][0] != null) {
                    //System.out.println("novo "+novo);

                    for (int l = 0; l < paginas.length; l++) {
                        //System.out.println(paginas[l][0] +" paginas" +" ->"+paginas[l][1] );
                        if (paginas[l][0] == novo) {
                            contem = true;
                            paginas[l][1] = 0;

                            //System.out.println("Contém Processo" + paginas[l][0] +" ponteiro "+ponteiro);
                            break;
                        }
                    }
                    if(contem){
                        //System.out.println("contém");
                        break;
                    }
                    if (paginas[j][1] == 0 && contem == false) {
                        //System.out.println("Não contém. Processo Atual: " + paginas[j][0]);
                        paginas[j][0] = novo;
                        paginas[j][1] = 1;
                        //System.out.println(" -- novo " + paginas[j][0]);
                        boolean bool = false;
                        ctrl2 = j;
                        if (ctrl2+ 1 > 7) {
                            bool = true;

                        }
                        if (ctrl2 + 2 > 7) {
                            j = 0;
                            if (bool)
                                j = 1;
                            paginas[j][1] = 0;
                        } else {
                            paginas[j + 2][1] = 0;
                        }

                        ponteiro++;
                        ponteiro = (ponteiro == 8) ? 0 : ponteiro;
                        //System.out.println(" -- ponteiro " + ponteiro);
                        break;
                    }
                }
            }
            for (int k = ponteiro; k < paginas.length; k++) {

                if (paginas[k][0] == null && contem == false) {
                    paginas[k][0] = novo;
                    //System.out.println("novo " + paginas[k][0] + " ponteiro " + ponteiro);
                    paginas[k][1] = 1;
                    boolean bool = false;
                    crtl = k;
                    if (crtl + 1 > 7) {
                        bool = true;
                        k = 0;
                        paginas[k][1] = 0;
                        //System.out.println("aqui");
                    } else {
                        paginas[k+1][1] = 0;
                    }
                    if (crtl + 2 > 7) {
                        k = 0;
                        if (bool)
                            k = 1;
                        paginas[k][1] = 0;
                    } else {
                        paginas[k + 2][1] = 0;
                    }

                    ponteiro++;
                    ponteiro = (ponteiro == 8) ? 0 : ponteiro;
                    //System.out.println(" --> ponteiro " + ponteiro);
                    break;
                }
            }


        }
        System.out.println("Páginas:");
        for (int i = 0; i <paginas.length ; i++) {
            System.out.println(paginas[i][0]);
        }
    }
}


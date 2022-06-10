package net.codejava.model;

import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import net.codejava.helper.*;

public class Block {
    private String[] transaction;
    private String blockHash;
    private String previousBlockHash;

    public Block(String[] transaction, String previousBlockHash) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        this.transaction = transaction;
        this.previousBlockHash = previousBlockHash;
        // this.blockHash = Arrays.hashCode(new String[] { Arrays.hashCode(transaction),
        // // this.previousBlockHash });

        this.blockHash = SHA256.getSHA(transaction,previousBlockHash);
    }

    public String[] getTransaction() {
        return transaction;
    }

    public void setTransaction(String[] transaction) {
        this.transaction = transaction;
    }

    public String getBlockHash() {
        return blockHash;
    }

    public void setBlockHash(String blockHash) {
        this.blockHash = blockHash;
    }

    public String getPreviousBlockHash() {
        return previousBlockHash;
    }

    public void setPreviousBlockHash(String previousBlockHash) {
        this.previousBlockHash = previousBlockHash;
    }

    @Override
    public String toString() {
        return "Block{" +
                "transaction=" + Arrays.toString(transaction) +
                ", blockHash=" + blockHash +
                ", previousBlockHash=" + previousBlockHash +
                '}';
    }
}

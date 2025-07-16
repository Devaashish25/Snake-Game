private void doDrawing(Graphics g) {
    if (inGame) {
        g.setColor(Color.red); // Set apple color to red
        g.fillOval(apple_x, apple_y, DOT_SIZE, DOT_SIZE);

        for (int z = 0; z < dots; z++) {
            if (z == 0) {
                g.setColor(Color.green); // Set snake color to green
                g.fillRect(x[z], y[z], DOT_SIZE, DOT_SIZE);
            } else {
                g.fillRect(x[z], y[z], DOT_SIZE, DOT_SIZE);
            }
        }

        Toolkit.getDefaultToolkit().sync();
    } else {
        gameOver(g);
    }
}
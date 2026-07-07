import pcbnew

def draw_nfc_coil(center_x_mm, center_y_mm, net_name_la, net_name_lb, turns=4, trace_width_mm=0.4, spacing_mm=0.4, start_w_mm=4, start_h_mm=16):
    board = pcbnew.GetBoard()
    width = pcbnew.FromMM(trace_width_mm)
    step = pcbnew.FromMM(trace_width_mm + spacing_mm)
    layer = pcbnew.F_Cu

    cx = pcbnew.FromMM(center_x_mm)
    cy = pcbnew.FromMM(center_y_mm)
    w = pcbnew.FromMM(start_w_mm) / 2
    h = pcbnew.FromMM(start_h_mm) / 2

    # Get or create nets
    netinfo = board.GetNetInfo()
    
    def get_net(name):
        net = netinfo.GetNetItem(name)
        if net is None:
            net = pcbnew.NETINFO_ITEM(board, name)
            board.Add(net)
        return net

    net_la = get_net(net_name_la)
    net_lb = get_net(net_name_lb)

    def add_track(x1, y1, x2, y2, net):
        track = pcbnew.PCB_TRACK(board)
        track.SetStart(pcbnew.VECTOR2I(int(x1), int(y1)))
        track.SetEnd(pcbnew.VECTOR2I(int(x2), int(y2)))
        track.SetWidth(width)
        track.SetLayer(layer)
        track.SetNet(net)
        board.Add(track)

    for i in range(turns):
        offset = i * step
        x0 = cx - w - offset
        x1 = cx + w + offset
        y0 = cy - h - offset
        y1 = cy + h + offset

        # Alternate nets per turn to approximate spiral connection
        net = net_la if i % 2 == 0 else net_lb

        add_track(x0, y1, x1, y1, net)   # bottom
        add_track(x1, y1, x1, y0, net)   # right
        add_track(x1, y0, x0, y0, net)   # top
        add_track(x0, y0, x0, y1 - step, net)  # left (spiral gap)

    pcbnew.Refresh()
    print("Coil drawn with nets assigned successfully")

# Undo old coils first, then run this
draw_nfc_coil(120.8375, 93.45, "/LINKEDIN_LA", "/LINKEDIN_LB", turns=4, trace_width_mm=0.4, spacing_mm=0.4, start_w_mm=4, start_h_mm=16)
draw_nfc_coil(194.4375, 93.45, "/EMAIL_LA", "/EMAIL_LB", turns=4, trace_width_mm=0.4, spacing_mm=0.4, start_w_mm=4, start_h_mm=16)